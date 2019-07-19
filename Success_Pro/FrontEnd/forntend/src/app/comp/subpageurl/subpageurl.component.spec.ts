import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SubpageurlComponent } from './subpageurl.component';

describe('SubpageurlComponent', () => {
  let component: SubpageurlComponent;
  let fixture: ComponentFixture<SubpageurlComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SubpageurlComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SubpageurlComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
