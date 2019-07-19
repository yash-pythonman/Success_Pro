import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegistationComponent } from './registation.component';

describe('RegistationComponent', () => {
  let component: RegistationComponent;
  let fixture: ComponentFixture<RegistationComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegistationComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegistationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
